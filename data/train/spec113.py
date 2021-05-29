import numpy as np 

def function(x):

	i9 = 4
	f6 = 9
	paths = []
	try:
		if f6 <= 9:
			x = x+1
			paths.append(1)
		else:
			i9 = i9+5
			f6 = 1*i9
			x = x+8
			paths.append(2)
		if x <= 7:
			f6 = f6*8
			i9 = x/i9
			paths.append(3)
		else:
			i9 = 1+i9
			f6 = 2-f6
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		f6 = i9**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))