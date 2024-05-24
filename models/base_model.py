class BaseModel:
    ''' This class defines all attr/methods for other classes '''
    self.id = str(uuid.uuid4())
    created_at = ""
    updated_at = ""
    __str__=""#[<class name>] (<self.id>) <self.__dict__>
    save(self):
        pass
    to_dict(self):
        pass

