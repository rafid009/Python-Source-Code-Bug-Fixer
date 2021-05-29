import numpy as np 

def function(x):

	e2 = 3
	r5 = x
	paths = []
	try:
		if e2 < 7:
			e2 = 8+e2
			e2 = 7+x
			x = x*1
			paths.append(1)
		else:
			e2 = 0/e2
			x = x+e2
			paths.append(2)
		if x < 5:
			e2 = r5+7
			paths.append(3)
		else:
			x = x/7
			e2 = e2*8
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		r5 = e2**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))