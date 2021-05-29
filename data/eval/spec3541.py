import numpy as np 

def function(x):

	j2 = x
	v8 = x
	paths = []
	try:
		if x >= 4:
			j2 = j2*v8
			x = 5+x
			v8 = 3+9
			paths.append(1)
		else:
			x = x/4
			j2 = j2+0
			paths.append(2)
		if v8 <= 3:
			j2 = j2*x
			j2 = j2/7
			j2 = x-j2
			paths.append(3)
		else:
			v8 = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))