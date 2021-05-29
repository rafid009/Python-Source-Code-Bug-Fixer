import numpy as np 

def function(x):

	f9 = x
	r6 = 6
	paths = []
	try:
		if f9 > 7:
			f9 = 4+r6
			x = r6/6
			paths.append(1)
		else:
			x = r6-x
			r6 = r6/r6
			paths.append(2)
		if f9 < 3:
			r6 = 4+1
			paths.append(3)
		else:
			r6 = r6+8
			r6 = r6/x
			x = 5*9
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		f9 = r6**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))