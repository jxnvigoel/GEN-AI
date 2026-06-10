from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
text='''def create_parking_slot(details):
    class ParkingSlot:
        def __init__(self,slot_id,hourly_rate):
            self.slot_id=slot_id
            self.hourly_rate=hourly_rate
            self.is_occupied=False
        def park(self):
            if self.is_occupied:
                return False
            else:
                self.is_occupied=True
                return True
        def leave(self,hours):
            if not self.is_occupied or hours<=0:
                return 0
            else:
                self.is_occupied=False
                return (self.hourly_rate*hours)
        def status(self):
            if self.is_occupied:
                return "Occupied"
            else:
                return "Empty"
    obj=ParkingSlot(details[0],details[1])
    return obj
    '''
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

result=splitter.split_text(text)

print(result[2])   
