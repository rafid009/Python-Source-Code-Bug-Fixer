import numpy as np 

def function(x):

	u3 = x
	b3 = x
	paths = []
	try:
		if u3 <= 4:
			b3 = b3+u3
			x = x-1
			paths.append(1)
		else:
			x = x-u3
			paths.append(2)
		if x > 5:
			u3 = u3-2
			u3 = u3*9
			x = x/9
			paths.append(3)
		else:
			b3 = 4-b3
			u3 = u3+0
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