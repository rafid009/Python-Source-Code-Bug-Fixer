import numpy as np 

def function(x):

	x2 = 4
	f7 = x
	paths = []
	try:
		if f7 < 0:
			f7 = f7-8
			x2 = 9-9
			paths.append(1)
		else:
			f7 = f7+x2
			x2 = x2+1
			paths.append(2)
		if x2 <= 2:
			f7 = 4*f7
			x2 = x2/6
			x2 = 0*x2
			paths.append(3)
		else:
			x2 = 5/1
			f7 = f7*2
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))