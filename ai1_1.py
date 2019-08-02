print("Enter Bill amount")
bamt=float(input())
cgst=float(0.09*bamt);
sgst=float(0.09*bamt);
print("CGST: "+str(cgst)+" SGST: "+str(sgst));
print("Total amount to be paid: "+str(bamt+cgst+sgst));

