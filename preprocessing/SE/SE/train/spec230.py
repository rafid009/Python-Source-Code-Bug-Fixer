import numpy as np 

def function(x):

	f5 = 2
	v5 = x
	x = x
	paths = []
	try:
		if v5 >= 3:
			v5 = v5-f5
			f5 = f5-f5
			f5 = 2-1
			paths.append(1)
		else:
			f5 = 6+6
			f5 = 1*f5
			paths.append(2)
		if v5 < 4:
			x = f5-1
			paths.append(3)
		else:
			v5 = 5+1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		f5 = v5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))