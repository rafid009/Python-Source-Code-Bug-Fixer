import numpy as np 

def function(x):

	o2 = 5
	u3 = 4
	paths = []
	try:
		if x <= 0:
			x = x/o2
			u3 = u3*x
			o2 = o2+1
			paths.append(1)
		else:
			o2 = 1+0
			x = o2*x
			u3 = u3-8
			paths.append(2)
		if x > 3:
			o2 = o2/8
			o2 = u3/1
			u3 = x/u3
			paths.append(3)
		else:
			o2 = o2*8
			u3 = o2/u3
			x = 7+u3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))