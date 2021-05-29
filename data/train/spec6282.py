import numpy as np 

def function(x):

	j2 = x
	i7 = x
	paths = []
	try:
		if j2 > 3:
			i7 = i7+9
			i7 = 9+i7
			x = 1/x
			paths.append(1)
		else:
			x = x*x
			j2 = 0+j2
			x = 0*2
			paths.append(2)
		if x <= 5:
			x = x*9
			j2 = j2*1
			i7 = i7-x
			paths.append(3)
		else:
			i7 = i7/6
			x = x-9
			i7 = i7*7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		j2 = i7**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))