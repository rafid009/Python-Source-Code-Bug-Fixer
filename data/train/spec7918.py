import numpy as np 

def function(x):

	f7 = x
	m5 = 5
	paths = []
	try:
		if f7 > 8:
			f7 = 6/5
			x = x*5
			paths.append(1)
		else:
			x = 1+1
			m5 = 7-m5
			paths.append(2)
		if f7 <= 6:
			f7 = f7-7
			paths.append(3)
		else:
			f7 = x-f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))