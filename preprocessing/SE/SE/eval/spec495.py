import numpy as np 

def function(x):

	f2 = x
	l6 = 0
	x = 5
	paths = []
	try:
		if l6 <= 5:
			f2 = 8+4
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x <= 6:
			f2 = l6+f2
			f2 = 0-f2
			x = x*0
			paths.append(3)
		else:
			f2 = x+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		l6 = f2**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))