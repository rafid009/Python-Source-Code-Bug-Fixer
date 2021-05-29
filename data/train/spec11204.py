import numpy as np 

def function(x):

	v9 = x
	o2 = x
	paths = []
	try:
		if v9 >= 7:
			v9 = v9*x
			o2 = x+5
			paths.append(1)
		else:
			o2 = o2/x
			o2 = x*5
			v9 = o2*3
			paths.append(2)
		if o2 > 8:
			x = o2+x
			o2 = 2+o2
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))