from lxml import etree

class AdvancedXMLParser:
    """基于lxml的高级XML解析器"""
    
    def __init__(self):
        self.parser = etree.XMLParser(remove_blank_text=True)
    
    def parse(self, xml_input, is_file=True):
        """
        解析XML输入
        
        Args:
            xml_input: XML字符串或文件路径
            is_file: 是否为文件路径
        """
        try:
            if is_file:
                tree = etree.parse(xml_input, self.parser)
            else:
                tree = etree.fromstring(xml_input, self.parser)
            
            return self._element_to_dict(tree.getroot() if is_file else tree)
        except etree.XMLSyntaxError as e:
            print(f"XML语法错误: {e}")
            return None
    
    def _element_to_dict(self, element):
        """将元素转换为字典"""
        result = {}
        
        # 命名空间处理
        tag = etree.QName(element).localname
        
        # 属性
        if element.attrib:
            result['@attributes'] = {
                etree.QName(k).localname: v for k, v in element.attrib.items()
            }
        
        # 文本内容
        if element.text and element.text.strip():
            result['#text'] = element.text.strip()
        
        # 子元素
        children = list(element)
        if children:
            for child in children:
                child_tag = etree.QName(child).localname
                child_data = self._element_to_dict(child)
                
                if child_tag in result:
                    if not isinstance(result[child_tag], list):
                        result[child_tag] = [result[child_tag]]
                    result[child_tag].append(child_data)
                else:
                    result[child_tag] = child_data
        
        # 如果没有属性、文本和子元素，返回简单值
        if not result and element.text:
            return element.text.strip()
        
        return result
    
    def xpath_query(self, xml_input, xpath_expression, is_file=False):
        """使用XPath查询XML"""
        try:
            if is_file:
                tree = etree.parse(xml_input, self.parser)
            else:
                tree = etree.fromstring(xml_input, self.parser)
            
            results = tree.xpath(xpath_expression)
            return [self._element_to_dict(result) if hasattr(result, 'tag') 
                   else str(result) for result in results]
        except etree.XPathError as e:
            print(f"XPath查询错误: {e}")
            return []