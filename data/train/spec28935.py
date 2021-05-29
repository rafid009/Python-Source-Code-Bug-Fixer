import numpy as np 

def function(x):

	f5 = 4
	j2 = 7
	paths = []
	try:
		if j2 >= 6:
			j2 = j2*x
			j2 = 9-j2
			paths.append(1)
		else:
			x = x+f5
			paths.append(2)
		if j2 > 0:
			j2 = j2*1
			x = f5-x
			j2 = j2-5
			paths.append(3)
		else:
			j2 = 9-j2
			j2 = j2*4
			x = x/9
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		f5 = j2**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))