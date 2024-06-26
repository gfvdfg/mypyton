std = { "name": "Phumi", "age":16, "gpa":3.5, "old_sch":"สาธิพัฒนา"}
print(std)
print("สวัสดีครับ %s" % std["name"])
print("อายุ %d เกรดเฉลี่ย %.2f จบจาก %s " % (std["age"] , std["gpa"], std["old_sch"]))

