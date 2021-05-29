import numpy as np 

def function(x):

	i9 = 6
	r2 = x
	paths = []
	try:
		if i9 >= 7:
			x = x-7
			paths.append(1)
		else:
			x = x*0
			i9 = r2*i9
			r2 = 4+1
			paths.append(2)
		if x <= 1:
			x = x-5
			r2 = r2+x
			paths.append(3)
		else:
			r2 = 7+x
			i9 = i9+2
			i9 = i9/i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))