import numpy as np 

def function(x):

	o2 = x
	v9 = 7
	paths = []
	try:
		if v9 >= 7:
			o2 = o2+o2
			o2 = 1*o2
			v9 = 5+9
			paths.append(1)
		else:
			v9 = v9*8
			o2 = o2/8
			paths.append(2)
		if x > 3:
			v9 = v9-4
			v9 = 2*v9
			v9 = o2+v9
			paths.append(3)
		else:
			o2 = o2*2
			v9 = v9-2
			o2 = 2/o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		v9 = o2**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))