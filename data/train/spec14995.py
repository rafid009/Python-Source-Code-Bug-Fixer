import numpy as np 

def function(x):

	f7 = 1
	m5 = 7
	paths = []
	try:
		if x < 1:
			x = x-5
			paths.append(1)
		else:
			m5 = m5-m5
			paths.append(2)
		if f7 > 4:
			m5 = 1/m5
			m5 = m5*6
			x = 3/x
			paths.append(3)
		else:
			f7 = m5+x
			m5 = m5*f7
			m5 = m5-5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))