#script addition concept for naming conventions on Verify Case screen
# this case will be created at the following location:

# extract information from elements of the form

print("what is patient name?")
name = input()
name_seperated = name.split(" ", 2)
last = name_seperated[0]
first_initial = name_seperated[1][0]
name_abbriviated = first_initial + last
# print(name_abbriviated)

print("what is surgeon name?")
surgeon = input()
surgeon_initials = surgeon.split(" ", 2)
surgeon_initials = surgeon_initials[0][0] + surgeon_initials[1][0]
# print(surgeon_initials)

print("what is case number?")
case = input()
remove_hyphen = case.replace("-", "")
# print(remove_hyphen)

print("what is procedure type?")
procedure = input()
if procedure == "TSA":
    implant = "VL"
if procedure =="RSA":
    implant = "MGS"
# print(implant)

filename = name_abbriviated + surgeon_initials + remove_hyphen + "_" + implant + ".ov-arthrex"
# path + filename 
path = "C:/DownloadedScans/" + case + "/" + filename
print(path)

