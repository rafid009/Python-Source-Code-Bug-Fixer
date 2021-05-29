import numpy as np 

def function(x):

	f1 = x
	k7 = 5
	paths = []
	try:
		if f1 >= 8:
			f1 = 6+f1
			x = k7*x
			f1 = 2+k7
			paths.append(1)
		else:
			x = 6/x
			f1 = f1+3
			paths.append(2)
		if k7 >= 1:
			k7 = k7*2
			f1 = f1+4
			k7 = k7*0
			paths.append(3)
		else:
			f1 = 2+k7
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))