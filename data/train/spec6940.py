import numpy as np 

def function(x):

	p1 = 7
	o2 = 5
	paths = []
	try:
		if o2 >= 8:
			x = p1-p1
			p1 = p1*1
			paths.append(1)
		else:
			o2 = o2-x
			paths.append(2)
		if x < 6:
			o2 = o2/4
			p1 = 7*o2
			x = 3-2
			paths.append(3)
		else:
			x = x*6
			x = 1*0
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))