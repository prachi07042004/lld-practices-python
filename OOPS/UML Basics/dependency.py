''' 
Dependency is a weak relationship where one class temporarily uses or relies on other class. The dependency is usually through method parameters, return types, or remporary usage -not permanent ownership
"Class A uses Class B for a short time to do some work, then forgets about it"
ex: printer -----> document

Realisation -  a class impements the methods defined by an interface(contract).a dashed line with a hollow, triangular arrowhead pointing from the implementing class to the interface. It signifies an "implements" relationship, where a classifier realizes the contract defined by an interface.
'''

class Document:
  def __init__(self, title:str, content:str, pages:int):
    self.__title = title
    self.__content = content
    self.__pages = pages

  def get_title(self)->str:
    return self.__title
  
  def get_content(self)->str:
    return self.__content

  def get_pages(self)->int:
    return self.__pages
  

#Printer class (depends on document)
class Printer:
    def __init__(self, printer_name:str, printer_type:str)->None:
      self.__printer_name = printer_name
      self.__printer_type = printer_type

    def print_document(self, document: Document)->None:
      #Printer uses document object temporarily through method parameter
      #After printing, printer does not keep the document

      print(f"\n{'='*50}")
      print(f"Printer: {self.__printer_name} ({self.__printer_type})")
      print(f"\n{'='*50}")
      print(f"Printing document: {document.get_title()}")
      print(f"Total Pages: {document.get_pages()}")
      print(f"Printing document: {document.get_content()}")
      print(f"\n{'='*50}")
      print("Printing Completed\n")

    def get_printer_info(self) -> str:
      return f"Printer: {self.__printer_name}-({self.__printer_type})"
    
doc1: Document = Document(
  title = "Python tutorial",
  content="This is a beginers guide",
  pages = 10
)

office_printer:Printer = Printer("HP LaserJet", "Laser Printer")
office_printer.print_document(doc1)

#IMP: Printer does not store the documents!
#documents still exist independently
print(f"Document 1 still exist: {doc1.get_title()}")




