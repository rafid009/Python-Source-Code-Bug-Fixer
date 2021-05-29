import numpy as np 

def function(x):

	r1 = 2
	o1 = x
	paths = []
	try:
		if x < 3:
			r1 = 9*r1
			r1 = r1+9
			o1 = o1-4
			paths.append(1)
		else:
			x = x*o1
			paths.append(2)
		if o1 <= 7:
			o1 = o1*6
			x = 6+x
			o1 = 7/o1
			paths.append(3)
		else:
			r1 = 5+r1
			x = x+9
			o1 = x-o1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))