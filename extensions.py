filename = (input("Enter File Name: ")).lower().strip()


if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg" ) or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".zip" ):
    print("application/zip")
elif filename.endswith(".pdf" ):
    print("application/pdf")
elif filename.endswith(".txt" ):
    print("text/plain")
elif filename.endswith(".png" ):
    print("image/png")
else:
    print("application/octet-stream")
