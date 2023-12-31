import io
import pathlib
import requests
import zipfile


class ClientPortal():

    def does_clientportal_directory_exist(self) -> bool:
        """Used to determine if the clientportal folder exist.

        Returns:
        bool: `True` if it exists, `False` otherwise.
        """

        # Grab the clientportal folder.
        clientportal_folder: pathlib.Path = pathlib.Path(__file__).parent.joinpath(
            'clientportal.gw'
        ).resolve()

        return clientportal_folder.exists()

    def make_clientportal_directory(self) -> None:
        """Makes the clientportal.gw folder if it doesn't exist."""

        if not self.does_clientportal_directory_exist:
            clientportal_folder: pathlib.Path = pathlib.Path(__file__).parent.joinpath(
                'clientportal.gw'
            ).resolve()
            clientportal_folder.mkdir(parents=True)

    def download_folder(self) -> str:
        """Defines the folder to download the Client Portal to.

        Returns:
        str: The path to the folder.
        """

        # Define the download folder.
        download_folder = pathlib.Path(__file__).parent.joinpath(
            'clientportal.gw'
        ).resolve()

        return download_folder

    def download_client_portal(self) -> requests.Response:
        """Downloads the Client Portal from Interactive Brokers.

        Returns:
        requests.Response: A response object with clientportal content.
        """

        # Request the Client Portal
        response = requests.get(
            url='https://download2.interactivebrokers.com/portal/clientportal.gw.zip'
        )

        return response

    def create_zip_file(self, response_content: requests.Response) -> zipfile.ZipFile:
        """Creates a zip file to house the client portal content.

        Arguments:
        ----
        response_content (requests.Response): The response object with the 
            client portal content.

        Returns:
        ----
        zipfile.ZipFile: A zip file object with the Client Portal.
        """

        # Download the Zip File.
        zip_file_content = zipfile.ZipFile(
            io.BytesIO(response_content.content)
        )

        return zip_file_content

    def extract_zip_file(self, zip_file: zipfile.ZipFile) -> None:
        """Extracts the Zip File.

        Arguments:
        ----
        zip_file (zipfile.ZipFile): The client portal zip file to be extracted.
        """

        # Extract the Content to the new folder.
        zip_file.extractall(path="clientportal.gw")

    def download_and_extract(self) -> None:
        """Downloads and extracts the client portal object."""

        # Make the resource directory if needed.
        self.make_clientportal_directory()

        # Download it.
        client_portal_response = self.download_client_portal()

        # Create a zip file.
        client_portal_zip = self.create_zip_file(
            response_content=client_portal_response
        )

        # Extract it.
        self.extract_zip_file(zip_file=client_portal_zip)
