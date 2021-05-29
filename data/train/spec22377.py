import numpy as np 

def function(x):

	i1 = 6
	f5 = x
	paths = []
	try:
		if i1 > 4:
			i1 = 1*f5
			f5 = f5+f5
			i1 = 1/x
			paths.append(1)
		else:
			x = i1/5
			i1 = i1-8
			f5 = 7+2
			paths.append(2)
		if f5 < 5:
			i1 = i1-4
			paths.append(3)
		else:
			f5 = 2-f5
			f5 = f5*0
			f5 = 0+9
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		f5 = i1**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))