import numpy as np 

def function(x):

	k1 = 6
	f6 = 5
	paths = []
	try:
		if f6 >= 7:
			x = x+x
			x = 3+2
			k1 = 3/k1
			paths.append(1)
		else:
			k1 = f6*0
			k1 = k1/1
			f6 = f6-8
			paths.append(2)
		if k1 <= 6:
			k1 = k1-3
			x = 6/1
			paths.append(3)
		else:
			x = x+k1
			x = x*5
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		f6 = k1**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))