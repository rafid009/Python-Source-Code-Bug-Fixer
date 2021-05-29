import numpy as np 

def function(x):

	j2 = 9
	f4 = x
	x = 6
	paths = []
	try:
		if x > 2:
			j2 = 2/2
			j2 = j2*1
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if j2 <= 0:
			x = f4+x
			paths.append(3)
		else:
			j2 = j2/1
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))