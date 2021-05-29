import numpy as np 

def function(x):

	f1 = 7
	w6 = 9
	paths = []
	try:
		if f1 >= 4:
			f1 = 4-f1
			w6 = w6/f1
			paths.append(1)
		else:
			f1 = w6*8
			paths.append(2)
		if w6 >= 3:
			w6 = w6+9
			f1 = 3-x
			paths.append(3)
		else:
			w6 = 2*0
			f1 = w6+6
			f1 = f1*x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))