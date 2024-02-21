import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { lastValueFrom } from 'rxjs';
import { environment } from '../../environment/environment';


@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  fileName = ""
  fileSize = 0
  fileType = ""
  chunks = 0

  constructor(
    private http: HttpClient
  ) { }

  async upload(event: Event) {
    const files = (event.target as HTMLInputElement).files

    if (!files || files.length < 1) {
      console.warn("select a file")
    }

    const file = files![0]
    const fileSize = file.size

    const KB = 1024
    const MB = 1024 * KB

    const maxSize = 5 * MB
    // const maxSize = 200 * KB

    const chunks = Math.ceil(fileSize / maxSize)

    this.fileName = file.name
    this.fileSize = file.size
    this.fileType = file.type
    this.chunks = chunks

    const FILE_PREFIX = "some_folder"
    const BUCKET = "destination_bucket_20_02_2024"
    const UPLOAD_URL = environment.uploadUrl

    for (let chunk = 0; chunk != chunks; chunk++) {

      const headers = new HttpHeaders(
        {
          'Content-Type': "application/upload-chunk",
          'x-amz-meta-chunk-range': `${chunk + 1}/${chunks}`,
          'x-amz-meta-file-prefix': FILE_PREFIX,
          'x-amz-meta-bucket': BUCKET,
        }
      )

      let start = maxSize * chunk
      let end = maxSize * (chunk + 1)

      await lastValueFrom(this.http.post(`${UPLOAD_URL}/${chunk + 1}-${file.name}`, file.slice(start, end), { headers: headers }))

    }

  }

}
