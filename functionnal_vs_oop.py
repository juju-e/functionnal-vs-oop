import os

class Files_methods():              # in OOP we use class which is a blueprint for the object.
  def __init__(self,cwd):          # we need to create a constructor for class variables(instance)
     self.cwd=cwd                   #  self represents the instance of the class. By using the self keyword we can access the attributes and methods of the class in python
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


def get_files_types(fun): # with functionnal programming, no need to make a blueprint and there are no private methods
  def decorate(type,cwd): # This function inside a function is called a nested function
     type,cwd=fun(type,cwd)  # we get the values 
     return list(filter(lambda word: word.endswith(type),os.listdir(cwd))) # used some common things used in functionnal programming
  return decorate  # a decorator returns functions
@get_files_types # we use this to specify a decorator to be applied on get_args.
def get_args(type,cwd):   
  return type,cwd

def transform_all_types_to(cwd,initial_type,final_type): 
      new=None
      old=None
      list=get_args(initial_type,cwd) # we can get the values by using this method
      for el in list:
          old=open(el,'r').read()
          os.remove(el)
          new=open(el.split(initial_type)[0]+final_type,'w')
          new.write(old)
          print(el.split(initial_type)[0]+final_type)

File=Files_methods('.')  # file is an object(instance) of the Files_method cless, we need to give the arguments of the constructor when declaring it.
print(File.print_files_types('.py')) # we access this method because it's public
File.transform_all_types_to('.pyw','.py') # convert all .pyw files to .py files
#Now let's look at functionnal programming;
# This call is equivalent to call to get_files_types with function "get_args('.py','.')" as the parameter 
print get_args('.py','.')
transform_all_types_to('.','.dfr','.opml')
