import os

class Files_methods():              # in OOP we use class which is a blueprint for the object.
  def __init__(self,cwd):          # we need to create a constructor for class variables(instance)
     self.cwd=cwd                   #  self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python
  def __get_files_types(self,type):       # we need to specify that the function can be called outside of the class by using self, i made this method private
     return [s for s in os.listdir(self.cwd) if s.endswith(type)] # cwd became like a global variable inside the class  
  def print_files_types(self,type):     
     return "\n".join(self.__get_files_types(type)) 
  def transform_all_types_to(self,initial_type,final_type): 
      self.new=None
      self.old=None
      list=self.__get_files_types(initial_type)
      for el in list:
          self.old=open(el,'r').read()
          os.remove(el)
          self.new=open(el.split(initial_type)[0]+final_type,'w')
          self.new.write(self.old)
          print(el.split(initial_type)[0]+final_type)


def get_files_types(type,cwd): # with functionnal programming, no need to make a blueprint and there are no private methods
 return list(filter(lambda word: word.endswith(type),os.listdir(cwd))) # used some common things used in functionnal programming
def print_files_types(type,cwd):
   return "\n".join(get_files_types(type,cwd)) # when we call functions, no need to put 'self' in the arguments
def transform_all_types_to(initial_type,final_type,cwd): # This function just transforms a file type to another( for text)
 new=None
 old=None
 list=get_files_types(initial_type,cwd)
 for el in list:
          old=open(el,'r').read()
          os.remove(el)
          new=open(el.split(initial_type)[0]+final_type,'w')
          new.write(self.old)
          print(el.split(initial_type)[0]+final_type)
File=Files_methods('.')  # file is an object(instance) of the Files_method cless, we need to give the arguments of the constructor when declaring it.
print(File.print_files_types('.py')) # we access this method because it's public
File.transform_all_types_to('.pyw','.py') # convert all .pyw files to .py files
#Now let's look at functionnal programming;
v=get_files_types('.py','.') # i can access this function when i want because there is no such thing as a private function inside the same file, the only thing possible is to make it non-callable when not in the main file with if __name__='__main__'
print(v) # will print the list
# we need to specify the cwd variable if it's not made global inside the whole file
transform_all_types_to('.pyw','.py','.')
