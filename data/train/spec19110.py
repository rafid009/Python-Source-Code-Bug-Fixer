import numpy as np 

def function(x):

	x6 = x
	e6 = x
	paths = []
	try:
		if e6 <= 1:
			e6 = e6*0
			paths.append(1)
		else:
			e6 = 1-2
			paths.append(2)
		if x > 4:
			x = x+1
			e6 = e6+e6
			x = 6*8
			paths.append(3)
		else:
			x6 = x6-5
			x = x*5
			x = x-x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x6 = e6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))