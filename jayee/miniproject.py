name=input("Name of the student:")
date=input("date")
classteacher=input("Classteacher name")
course=input("course name")
reason=input("reason for leave")
place=input("place")
leave=input("leave date")
newstring=f'''
    From
    {name}
    {course}
    {place}
    To
    {classteacher}
    {course}
    {place}
    
    Dear sir/mam,
          I am {name},a student of {course}.I would like to inform you that, {reason}.
          so Irequested to you kindly allow me to take leave from {leave}
                                
                                Thank You
    
    Regards
    
    (signature)
    {name}'''
print(newstring)
 