import numpy as np 

def function(x):

	u3 = x
	o1 = x
	paths = []
	try:
		if u3 <= 3:
			x = 3/x
			paths.append(1)
		else:
			o1 = u3/5
			o1 = o1/4
			u3 = o1*4
			paths.append(2)
		if x > 7:
			u3 = u3/7
			o1 = 9+0
			paths.append(3)
		else:
			x = 6/x
			x = x*o1
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))