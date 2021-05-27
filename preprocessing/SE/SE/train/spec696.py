import numpy as np 

def function(x):

	i7 = x
	q9 = x
	paths = []
	try:
		if i7 >= 2:
			q9 = q9+4
			i7 = x+2
			paths.append(1)
		else:
			q9 = q9/5
			x = q9*8
			x = x*1
			paths.append(2)
		if q9 < 8:
			i7 = i7/1
			x = x/9
			x = x+7
			paths.append(3)
		else:
			x = x-0
			i7 = i7+1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		i7 = q9**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))