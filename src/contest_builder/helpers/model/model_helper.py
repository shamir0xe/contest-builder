class ModelHelper:
    @staticmethod
    def get_model_attributes(Model) -> list:
        return list(filter(lambda key: "__" != key[:2], Model.__dict__.keys()))
