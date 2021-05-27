import numpy as np 

def function(x):

	f3 = x
	j0 = x
	paths = []
	try:
		if j0 <= 7:
			j0 = 0+j0
			paths.append(1)
		else:
			f3 = 2-7
			paths.append(2)
		if f3 < 9:
			f3 = f3*5
			j0 = j0/f3
			f3 = f3/9
			paths.append(3)
		else:
			j0 = j0+6
			j0 = j0/7
			f3 = f3*1
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		f3 = j0**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))