import numpy as np 

def function(x):

	u3 = x
	e2 = 4
	paths = []
	try:
		if u3 < 5:
			e2 = e2*2
			paths.append(1)
		else:
			e2 = e2*1
			e2 = u3-3
			paths.append(2)
		if u3 < 4:
			e2 = e2*0
			paths.append(3)
		else:
			e2 = e2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))