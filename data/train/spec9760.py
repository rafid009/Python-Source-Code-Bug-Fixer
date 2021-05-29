import numpy as np 

def function(x):

	v9 = x
	f1 = 2
	paths = []
	try:
		if v9 < 0:
			v9 = x*2
			x = 7+x
			x = 6/x
			paths.append(1)
		else:
			f1 = x/f1
			paths.append(2)
		if v9 > 7:
			v9 = 9*v9
			paths.append(3)
		else:
			v9 = x/v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		f1 = v9**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))