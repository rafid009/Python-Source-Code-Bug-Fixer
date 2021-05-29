import numpy as np 

def function(x):

	y6 = x
	e2 = 5
	x = 4
	paths = []
	try:
		if x < 8:
			e2 = y6+3
			e2 = e2*4
			y6 = y6-6
			paths.append(1)
		else:
			e2 = e2+3
			x = x*1
			paths.append(2)
		if e2 <= 4:
			e2 = e2/6
			y6 = 8-7
			y6 = y6/3
			paths.append(3)
		else:
			x = x*8
			e2 = 7*0
			e2 = e2-3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))