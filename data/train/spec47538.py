import numpy as np 

def function(x):

	o5 = 5
	u1 = x
	x = x
	paths = []
	try:
		if x > 0:
			o5 = o5-u1
			o5 = x*o5
			u1 = u1-3
			paths.append(1)
		else:
			x = 7*0
			x = x+u1
			u1 = x*5
			paths.append(2)
		if x >= 9:
			u1 = 4/u1
			paths.append(3)
		else:
			x = x+x
			x = x+1
			x = u1+o5
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		o5 = u1**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))