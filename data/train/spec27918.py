import numpy as np 

def function(x):

	m5 = 1
	o8 = 0
	paths = []
	try:
		if o8 <= 7:
			o8 = o8/7
			o8 = o8+x
			paths.append(1)
		else:
			m5 = m5-9
			m5 = x-x
			paths.append(2)
		if x > 7:
			x = 6-0
			paths.append(3)
		else:
			x = o8-x
			m5 = x-m5
			x = x-7
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		m5 = o8**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))