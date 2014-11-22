#For the AwesomeGroupList
#colaborator-John Hernandez <johnhndzr@gmail.com>


#This is gonna be the class of each video to our awesome playlist

class Video():
	
	"""Class made by the group for make some playlist fucking awesomes"""
	
	def __init__(self, **valores):

	    self.category = valores.get("category")
	    self.quality = valores.get("quality")
	    self.name = valores.get("name")
	    self.duration = valores.get("duration")
	    self.autor = valores.get("autor")
	    self.age_class = valores.get("age_class")
	    self.subtitle = valores.get("subtitle")
	    self.like = valores.get("like")
	    self.partners = valores.get("partners")
	    self.url = valores.get("url")
	    self.description = valores.get("description")
	    self.views = valores.get("views")
	    self.region_availability = valores.get("region_availability")
	    self.notation = valores.get("notation")
	    self.upload_date = valores.get("upload_date")
	    self.licence = valores.get("licence")
#Body to declarate the class
