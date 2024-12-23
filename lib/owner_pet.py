class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise Exception("Invalid pet type. Must be an instance of Pet")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if isinstance(owner, Owner):
            self.owner = owner
            owner.add_pet(self)
        elif owner is None:
            self.owner = None
        else:
            raise Exception("Owner must be an instance of Owner or None.") 
        
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception({"Invalid pet type"})
        
        self.all.append(self)



    