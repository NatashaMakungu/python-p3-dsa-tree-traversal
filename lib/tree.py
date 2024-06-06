class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if not self.root:
      return None
      
    node_to_visit = [self.root]
    while node_to_visit:
      current_node = node_to_visit.pop(0)
      if current_node['id'] == id:
        return current_node
        
      for child in current_node.get('children', []):
        node_to_visit.append(child)

    return None
