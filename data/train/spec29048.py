import numpy as np 

def function(x):

	o2 = 9
	e1 = 7
	paths = []
	try:
		if x > 6:
			x = x*0
			e1 = 3/4
			paths.append(1)
		else:
			e1 = 9*o2
			o2 = o2+1
			paths.append(2)
		if x > 6:
			o2 = o2-9
			o2 = 4-o2
			x = x+5
			paths.append(3)
		else:
			x = 3-x
			o2 = x/1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))