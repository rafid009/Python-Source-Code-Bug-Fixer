import numpy as np 

def function(x):

	o2 = x
	v8 = x
	paths = []
	try:
		if v8 > 1:
			o2 = 9-3
			o2 = o2*0
			paths.append(1)
		else:
			x = x*5
			o2 = o2+3
			o2 = o2+o2
			paths.append(2)
		if x > 6:
			v8 = v8*o2
			x = x*9
			o2 = o2+o2
			paths.append(3)
		else:
			x = 3-x
			o2 = 8*o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		v8 = o2**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))