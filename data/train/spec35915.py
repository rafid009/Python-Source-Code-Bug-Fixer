import numpy as np 

def function(x):

	w7 = x
	v5 = 3
	paths = []
	try:
		if x > 0:
			x = x-4
			w7 = w7-7
			w7 = 6/w7
			paths.append(1)
		else:
			w7 = 1*w7
			x = x+x
			x = 5*2
			paths.append(2)
		if v5 > 9:
			v5 = 5-v5
			v5 = v5/7
			x = 3+1
			paths.append(3)
		else:
			v5 = 0+v5
			x = x*3
			v5 = w7*v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))