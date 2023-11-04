FROM ubuntu:latest

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory for your scripts and data
RUN mkdir -p /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Copy your scripts into the container
COPY ./dpre.py /home/doc-bd-a1/
COPY ./eda.py /home/doc-bd-a1/
COPY ./vis.py /home/doc-bd-a1/
COPY ./model.py /home/doc-bd-a1/

# Copy the dataset into the container
COPY ./organization.csv /home/doc-bd-a1/

# Set the command to run when the container starts
CMD ["/bin/bash"]
