import numpy as np 

def function(x):

	j9 = 2
	f5 = x
	paths = []
	try:
		if j9 <= 6:
			f5 = f5+x
			paths.append(1)
		else:
			j9 = j9/4
			x = 4*1
			j9 = 4*9
			paths.append(2)
		if f5 > 3:
			j9 = 0*j9
			j9 = 8*j9
			x = x-x
			paths.append(3)
		else:
			x = 5-x
			x = x/f5
			j9 = j9-f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))